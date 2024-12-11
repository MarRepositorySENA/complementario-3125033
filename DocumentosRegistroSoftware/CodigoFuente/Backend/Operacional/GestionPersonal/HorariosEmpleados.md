```
//ENTITY HORARIOSEMPLEADOS
package com.persona.Backend.Entity.Operational.GestionPersonal;

import java.time.LocalDateTime;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Operational.GestionHorario.ProgramacionFicha;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "horario_empleado")
public class HorariosEmpleados extends BaseEntity {

	@Column(name = "hora_inicio", length = 45, nullable = false)
	private LocalDateTime horaInicio;

	@Column(name = "hora_fin", length = 45, nullable = false)
	private LocalDateTime horaFin;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "empleado_id", nullable = false, unique =false)
	private Empleado empleadoId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "programacion_ficha_id", nullable = false, unique = false)
	private ProgramacionFicha programacionFichaId;

	public LocalDateTime getHoraInicio() {
		return horaInicio;
	}

	public void setHoraInicio(LocalDateTime horaInicio) {
		this.horaInicio = horaInicio;
	}

	public LocalDateTime getHoraFin() {
		return horaFin;
	}

	public void setHoraFin(LocalDateTime horaFin) {
		this.horaFin = horaFin;
	}

	public Empleado getEmpleadoId() {
		return empleadoId;
	}

	public void setEmpleadoId(Empleado empleadoId) {
		this.empleadoId = empleadoId;
	}

	public ProgramacionFicha getProgramacionFichaId() {
		return programacionFichaId;
	}

	public void setProgramacionFichaId(ProgramacionFicha programacionFichaId) {
		this.programacionFichaId = programacionFichaId;
	}

}
//IREPOSITORY HORARIOSEMPLEADOS
package com.persona.Backend.IRepository.Operational.GestionPersonal;

import java.time.LocalDateTime;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionPersonal.HorariosEmpleados;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IHorariosEmpleadosRepository  extends IBaseRepository<HorariosEmpleados, Long>{


	@Query("SELECT COUNT(he) FROM HorariosEmpleados he WHERE he.empleadoId.id = :empleadoId AND " +
		       "(:horaInicio BETWEEN he.horaInicio AND he.horaFin OR :horaFin BETWEEN he.horaInicio AND he.horaFin OR " +
		       "he.horaInicio BETWEEN :horaInicio AND :horaFin OR he.horaFin BETWEEN :horaInicio AND :horaFin)")
		Long countConflictingEmpleados(@Param("empleadoId") Long empleadoId, 
		                               @Param("horaInicio") LocalDateTime horaInicio, 
		                               @Param("horaFin") LocalDateTime horaFin);

}
//ISERVICE HORARIOSEMPLEADOS 
package com.persona.Backend.IService.Operational.GestionPersonal;

import java.time.LocalDateTime;

import com.persona.Backend.Entity.Operational.GestionPersonal.HorariosEmpleados;
import com.persona.Backend.IService.IBaseService;

public interface IHorariosEmpleadosService extends IBaseService<HorariosEmpleados> {

	 boolean verificarConflictoEmpleado(Long empleadoId, LocalDateTime horaInicio, LocalDateTime horaFin);
}
//SERVICE HORARIOSEMPLEADOS
package com.persona.Backend.Service.Operational.GestionPersonal;

import java.time.LocalDateTime;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionPersonal.HorariosEmpleados;
import com.persona.Backend.IRepository.Operational.GestionPersonal.IHorariosEmpleadosRepository;
import com.persona.Backend.IService.Operational.GestionPersonal.IHorariosEmpleadosService;
import com.persona.Backend.Service.BaseService;

@Service
public class HorariosEmpleadosService extends BaseService<HorariosEmpleados> implements IHorariosEmpleadosService{
	 
	@Autowired
    private IHorariosEmpleadosRepository repository;

    @Override
    public boolean verificarConflictoEmpleado(Long empleadoId, LocalDateTime horaInicio, LocalDateTime horaFin) {
        Long conflictos = repository.countConflictingEmpleados(empleadoId, horaInicio, horaFin);
        return conflictos > 0;
    }

    @Override
    public HorariosEmpleados save(HorariosEmpleados horariosEmpleados) throws Exception {
        // Verificar si hay conflicto de horario antes de guardar
        boolean conflicto = verificarConflictoEmpleado(horariosEmpleados.getEmpleadoId().getId(),
                                                       horariosEmpleados.getHoraInicio(),
                                                       horariosEmpleados.getHoraFin());

        if (conflicto) {
            throw new Exception("Conflicto de horario detectado. No se puede guardar el registro.");
        }

        return repository.save(horariosEmpleados);  // Solo guarda si no hay conflicto
    }
}
//CONTROLLER HORARIOSEMPLEADOS
package com.persona.Backend.Controller.Operational.GestionPersonal;

import java.time.LocalDateTime;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.HttpStatus;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionPersonal.HorariosEmpleados;
import com.persona.Backend.IService.Operational.GestionPersonal.IHorariosEmpleadosService;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_personal/horarios_empleados")
public class HorariosEmpleadosController extends BaseController<HorariosEmpleados>{

	  @Autowired
	    private IHorariosEmpleadosService horariosEmpleadosService;

	    @GetMapping("/verificar-conflicto")
	    public ResponseEntity<String> verificarConflictoEmpleado(
	            @RequestParam Long empleadoId,
	            @RequestParam LocalDateTime horaInicio,
	            @RequestParam LocalDateTime horaFin) {

	        boolean conflicto = horariosEmpleadosService.verificarConflictoEmpleado(empleadoId, horaInicio, horaFin);

	        if (conflicto) {
	            return ResponseEntity.status(HttpStatus.CONFLICT).body("Conflicto de horario con el instructor.");
	        }

	        return ResponseEntity.ok("No hay conflictos con el instructor.");
	    }
}




```