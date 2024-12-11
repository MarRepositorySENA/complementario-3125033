```
//ENTITY HORARIOSAMBIENTES
package com.persona.Backend.Entity.Operational.GestionHorario;

import java.time.LocalDateTime;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Parameter.Infraestrutura.Ambiente;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name="horarios_ambientes")
public class HorariosAmbientes extends BaseEntity{
	

	@Column(name = "hora_inicio", length = 45, nullable = false)
	private LocalDateTime horaInicio;

	@Column(name = "hora_fin", length = 45, nullable = false)
	private LocalDateTime horaFin;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "ambiente_id", nullable = false, unique = false)
	private Ambiente ambienteId;

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

	public Ambiente getAmbienteId() {
		return ambienteId;
	}

	public void setAmbienteId(Ambiente ambienteId) {
		this.ambienteId = ambienteId;
	}

	public ProgramacionFicha getProgramacionFichaId() {
		return programacionFichaId;
	}

	public void setProgramacionFichaId(ProgramacionFicha programacionFichaId) {
		this.programacionFichaId = programacionFichaId;
	}

	
	
}
//IREPOSITORY HORARIOSAMBIENTES
package com.persona.Backend.IRepository.Operational.GestionHorario;

import java.time.LocalDateTime;
import java.util.List;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionHorario.HorariosAmbientes;
import com.persona.Backend.Entity.Operational.GestionPersonal.HorariosEmpleados;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IHorariosAmbientesRepository extends IBaseRepository<HorariosAmbientes, Long> {

	@Query("SELECT COUNT(ha) FROM HorariosAmbientes ha WHERE ha.ambienteId.id = :ambienteId AND " +
		       "(:horaInicio BETWEEN ha.horaInicio AND ha.horaFin OR :horaFin BETWEEN ha.horaInicio AND ha.horaFin OR " +
		       "ha.horaInicio BETWEEN :horaInicio AND :horaFin OR ha.horaFin BETWEEN :horaInicio AND :horaFin)")
		Long countConflictingAmbientes(@Param("ambienteId") Long ambienteId, 
		                               @Param("horaInicio") LocalDateTime horaInicio, 
		                               @Param("horaFin") LocalDateTime horaFin);

}
//ISERVICE HORARIOSAMBIENTES
package com.persona.Backend.IService.Operational.GestionHorario;

import java.time.LocalDateTime;
import java.util.List;

import com.persona.Backend.Entity.Operational.GestionHorario.HorariosAmbientes;
import com.persona.Backend.Entity.Operational.GestionPersonal.HorariosEmpleados;
import com.persona.Backend.IService.IBaseService;

public interface IHorariosAmbientesService extends IBaseService<HorariosAmbientes> {

	boolean verificarConflictoAmbiente(Long ambienteId, LocalDateTime horaInicio, LocalDateTime horaFin);

}
//SERVICE HORARIOSAMBIENTES
package com.persona.Backend.Service.Operational.GestionHorario;

import java.time.LocalDateTime;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionHorario.HorariosAmbientes;
import com.persona.Backend.Entity.Operational.GestionPersonal.HorariosEmpleados;
import com.persona.Backend.IRepository.Operational.GestionHorario.IHorariosAmbientesRepository;
import com.persona.Backend.IRepository.Operational.GestionPersonal.IHorariosEmpleadosRepository;
import com.persona.Backend.IService.Operational.GestionHorario.IHorariosAmbientesService;
import com.persona.Backend.Service.BaseService;

@Service
public class HorariosAmbientesService extends BaseService<HorariosAmbientes> implements IHorariosAmbientesService{

	  @Autowired
	    private IHorariosAmbientesRepository repository;

	    @Override
	    public boolean verificarConflictoAmbiente(Long ambienteId, LocalDateTime horaInicio, LocalDateTime horaFin) {
	        Long conflictos = repository.countConflictingAmbientes(ambienteId, horaInicio, horaFin);
	        return conflictos > 0;
	    }

	    @Override
	    public HorariosAmbientes save(HorariosAmbientes horariosAmbientes) throws Exception {
	        // Verificar si hay conflicto de horario antes de guardar
	        boolean conflicto = verificarConflictoAmbiente(horariosAmbientes.getAmbienteId().getId(),
	                                                      horariosAmbientes.getHoraInicio(),
	                                                      horariosAmbientes.getHoraFin());

	        if (conflicto) {
	            throw new Exception("Conflicto de horario detectado. No se puede guardar el registro.");
	        }

	        return repository.save(horariosAmbientes);  // Solo guarda si no hay conflicto
	    }
}
//CONTROLLER HORARIOSAMBIENTES
package com.persona.Backend.Controller.Operational.GestionHorario;

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
import com.persona.Backend.Entity.Operational.GestionHorario.HorariosAmbientes;
import com.persona.Backend.IService.Operational.GestionHorario.IHorariosAmbientesService;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_horario/horarios_ambientes")
public class HorariosAmbientesController extends BaseController<HorariosAmbientes> {

	  @Autowired
	    private IHorariosAmbientesService horariosAmbientesService;

	    @GetMapping("/verificar-conflicto")
	    public ResponseEntity<String> verificarConflictoAmbiente(
	            @RequestParam Long ambienteId,
	            @RequestParam LocalDateTime horaInicio,
	            @RequestParam LocalDateTime horaFin) {

	        boolean conflicto = horariosAmbientesService.verificarConflictoAmbiente(ambienteId, horaInicio, horaFin);

	        if (conflicto) {
	            return ResponseEntity.status(HttpStatus.CONFLICT).body("Conflicto de horario en el ambiente.");
	        }

	        return ResponseEntity.ok("No hay conflictos en el ambiente.");
	    }
	
}


```