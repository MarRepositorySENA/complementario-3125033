```
//ENTITY FICHA
package com.persona.Backend.Entity.Operational.GestionHorario;

import java.time.LocalDate;
import java.time.LocalDateTime;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Operational.GestionFormativa.ProgramaFormacion;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;

@Entity
@Table(name="ficha")
public class Ficha extends BaseEntity{
	
	@Column(name = "codigo", length = 40, nullable = false)
	private String codigo;

	@Column(name = "fecha_inicio",  nullable = false)
	private LocalDate fechaInicio;
	
	@Column(name = "fecha_fin",  nullable = false)
	private LocalDate fechaFin;
	
	@Column(name = "cupo",  nullable = false)
	private Integer cupo;
	
	@Column(name = "etapa",  nullable = false)
	private String etapa;
	
	@ManyToOne	(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "jornada_id", nullable = false, unique = false)
	private Jornada jornadaId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "convocatoria_id", nullable = false, unique = false)
	private Convocatoria convocatoriaId;
	
	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "programa_formacion_id", nullable = false, unique = false)
	private ProgramaFormacion programaFormacionId;

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public LocalDate getFechaInicio() {
		return fechaInicio;
	}

	public LocalDate getFechaFin() {
		return fechaFin;
	}

	public void setFechaFin(LocalDate fechaFin) {
		this.fechaFin = fechaFin;
	}

	public void setFechaInicio(LocalDate fechaInicio) {
		this.fechaInicio = fechaInicio;
	}

	public Integer getCupo() {
		return cupo;
	}

	public void setCupo(Integer cupo) {
		this.cupo = cupo;
	}

	public String getEtapa() {
		return etapa;
	}

	public void setEtapa(String etapa) {
		this.etapa = etapa;
	}

	public Jornada getJornadaId() {
		return jornadaId;
	}

	public void setJornadaId(Jornada jornadaId) {
		this.jornadaId = jornadaId;
	}

	public Convocatoria getConvocatoriaId() {
		return convocatoriaId;
	}

	public void setConvocatoriaId(Convocatoria convocatoriaId) {
		this.convocatoriaId = convocatoriaId;
	}

	public ProgramaFormacion getProgramaFormacionId() {
		return programaFormacionId;
	}

	public void setProgramaFormacionId(ProgramaFormacion programaFormacionId) {
		this.programaFormacionId = programaFormacionId;
	}


}
//IREPOSITORY FICHA
package com.persona.Backend.IRepository.Operational.GestionHorario;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionHorario.Ficha;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IFichaRepository extends IBaseRepository<Ficha, Long> {

}
//ISERVICE FICHA
package com.persona.Backend.IService.Operational.GestionHorario;

import com.persona.Backend.Entity.Operational.GestionHorario.Ficha;
import com.persona.Backend.IService.IBaseService;

public interface IFichaService extends IBaseService<Ficha>{

}
//SERVICE FICHA
package com.persona.Backend.Service.Operational.GestionHorario;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionHorario.Ficha;
import com.persona.Backend.IService.Operational.GestionHorario.IFichaService;
import com.persona.Backend.Service.BaseService;

@Service
public class FichaService extends BaseService<Ficha> implements IFichaService{

}
//CONTROLLER FICHA
package com.persona.Backend.Controller.Operational.GestionHorario;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionHorario.Ficha;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_horario/ficha")
public class FichaController extends BaseController<Ficha>{

}

```